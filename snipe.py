#!/usr/bin/python

import sys
import argparse
import logging
import time

import pogo.util as util
from pogo.api import PokeAuthSession
from pogo.inventory import items
from pogo.pokedex import pokedex


def findByName(session, name):

    cells = session.getMapObjects(bothDirections=False)

    for cell in cells.map_cells:
        pokemons = [p for p in cell.catchable_pokemons]

        for pokemon in pokemons:
            if pokedex[pokemon.pokemon_id] == name:
                return pokemon
    return None


def catch(session, encounter, pokemon):

    if encounter.status == encounter.POKEMON_INVENTORY_FULL:
        logging.error("Can't catch! Party is full!")

    balls = [items.ULTRA_BALL, items.GREAT_BALL, items.POKE_BALL]

    for count in range(0, 5):
        n_berry = session.inventory.bag.get(items.RAZZ_BERRY, 0)

        if n_berry > 0:
            logging.info("Using Razz Berry")
            session.useItemCapture(items.RAZZ_BERRY, pokemon)
            time.sleep(2)

        available_ball = None
        
        for ball in balls:
            if session.inventory.bag.get(ball, 0) > 0:
                available_ball = ball
                break

        if available_ball:
            logging.info("Using " + items[available_ball])
            attempt = session.catchPokemon(pokemon, available_ball)
            time.sleep(3)

            if attempt.status == 1:
                logging.info("Success. Caught a " + pokedex[pokemon.pokemon_id])
                for poke in session.getInventory().party:
                    if poke.id == attempt.captured_pokemon_id:
                        logging.info(poke)
                return
            
            if attempt.status == 3:
                if count == 0:
                    logging.info("Possible soft ban")
                else:
                    logging.info("Fleed at %d attempt" % (count+1))
                return
    return


def snipe(session, olat, olng, lat, lng, name):

    # teleport
    session.setCoordinates(lat, lng)

    # wait 10s
    time.sleep(10)

    logging.info("Looking for " + name + " at " + str(lat) + ", " + str(lng))

    pokemon = findByName(session, name)
    encounter = None

    # found
    if pokemon:
        encounter = session.encounterPokemon(pokemon)
    else:
        logging.info(name + " not found.")

    # teleport back
    session.setCoordinates(olat, olng)

    if encounter:
        catch(session, encounter, pokemon)


if __name__ == '__main__':
    util.setupLogger()
    logging.debug('Logger set up')

    # Read in args
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--auth", help="Auth Service", required=True)
    parser.add_argument("-u", "--username", help="Username", required=True)
    parser.add_argument("-p", "--password", help="Password", required=True)
    parser.add_argument("-e", "--encrypt_lib", help="Encryption Library")
    parser.add_argument("-g", "--geo_key", help="GEO API Secret")
    parser.add_argument("-l", "--location", help="Location")
    parser.add_argument("-proxy", "--proxy", help="Full Path to Proxy")
    args = parser.parse_args()

    # Check service
    if args.auth not in ['ptc', 'google']:
        logging.debug("Invalid auth service %s", args.auth)
        exit()

    # Create PokoAuthObject
    auth_session = PokeAuthSession(
            args.username,
            args.password,
            args.auth,
            args.encrypt_lib,
            geo_key=args.geo_key,
            )

    if 'location' not in args:
        exit()

    # create session with location
    session = auth_session.authenticate(locationLookup=args.location)
    
    # remember the current latitude, longiude, altitude
    (olat, olng, oalt) = session.getCoordinates()

    if session:
        while True:
            try:
                print "Location -> ",
                (lat, lng) = raw_input().split(',')

                print "Name -> ",
                name = raw_input().upper().strip()

                snipe(session, olat, olng, float(lat), float(lng), name)
            except ValueError:
                print "Unexpected error: ", sys.exc_info()[0]
                continue
