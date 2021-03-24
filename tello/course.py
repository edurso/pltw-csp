from tello import Drone
drone = Drone()
drone.interactive_loop_cli()
drone.kill()