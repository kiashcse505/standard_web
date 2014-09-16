from fabric.api import lcd, sudo, local, cd, hosts
from fabric.colors import green, red, blue
from fabric.contrib import django

django.project('mhealth_web')
django.settings_module('mhealthcare.settings')

def test():
    local("./manage.py test my_app")

def commit(local_branch_name="ridwan_current"):
    local('git add -p && git commit')
    local('git checkout master && git merge ' + local_branch_name)

def push(production_branch_name="ridwan_current"):
    local("git push origin" + production_branch_name)

def prepare_deploy():
    local_branch_name = raw_input("enter your local git branch name: ")
    production_branch_name = raw_input("enter your production branch name to push to: ")
    #test()
    commit(local_branch_name)
    push(production_branch_name)


def server_reboot():
    "Reboot Apache2 server."
    sudo("apache2ctl graceful")

def deploy():
    code_dir = '/var/www/mhealth_web'
    repo_url = 'http://182.160.102.170:8081/p/mhealth_web_protal.git'

    sudo('su apps')

    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone %s %s" % (repo_url,code_dir))
    with cd(code_dir):
        branch_name = raw_input("enter your git branch name to pull from: ")
        run("git pull origin " + branch_name)
        local('python manage.py migrate')
        #local('python manage.py test myapp')
        server_reboot()


def hello():
    name = raw_input("enter your name: ")
    title = raw_input("enter your title: ")
    print("Hello %s %s!" % (title,name))
    #print "Hello, World!"