import routes
from rider import application

if __name__ == '__main__':
    from rider.utils import server
    server.run(application)
