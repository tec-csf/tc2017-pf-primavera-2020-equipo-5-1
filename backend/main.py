import star_topology
import time

def main():
    c = star_topology.Central(3, 4, 4, 4, 100)
    c.turn_on()
    time.sleep(50)
    c.turn_off()


if __name__ == '__main__':
    main()