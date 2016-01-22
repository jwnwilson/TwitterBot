from fabric.api import local


def run_manage(command):
    local('python ./manage.py %s' % command)


def web():
    run_manage('runserver 0.0.0.0:8888')


def docker_compose():
    local("docker-compose up")


def docker_ip(machine_name="default"):
    """
    Run with 'fab docker_ip:$MACHINE_NAME'
    :param machine_name: docker image name
    :return: ip address of docker instance to connect to in a browser
    """
    local("docker-machine ip %s" % machine_name)

def migrate():
    run_manage('migrate')


def make_migrations():
    run_manage('makemigrations')


def requirements():
    local('pip install -r requirements.txt ')


def test():
    run_manage('test items stream')


def create_test_data():
    run_manage('dumpdata stream items auth.user --indent 2 > testsite/test_data.json')


def clear_load_test():
    # Clear data
    run_manage('flush')
    # Syncdb
    #run_manage('syncdb')
    # Load Data
    run_manage('loaddata testsite/test_data.json')