#!/usr/bin/env python
import os, getopt, sys, subprocess

IMAGE_NAME = "test_redis"

def build_image():
    subprocess.call(["docker", "build", "-t", IMAGE_NAME, "."])

def delete_image():
    subprocess.call(["docker", "rmi", IMAGE_NAME])

#def start():
    #TODO : start command

def usage():
    print "usage"

if __name__ == '__main__':
    # Get opts
    try:
        long_args = ["image"]
        opts, args = getopt.getopt(sys.argv[1:], "be:he:s:c:r:", long_args)
    except getopt.GetoptError as err:
        print "opt err: ", str(err)
        usage()
        sys.exit(2)

    # Check options
    for o, a in opts:
        if o in ("--image"):
            for a in args:
                if a in ("build"):
                    build_image()
                if a in ("delete"):
                    delete_image()

