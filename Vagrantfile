# -*- mode: ruby -*-
# vi: set ft=ruby :

###############################################################################
#                                                                             #
# Vagrantfile project: towan                                                  #
# Description:                                                                #
# Dev environement for Django app provision with docker postgresql container  #
# and his data container                                                      #
# Author: Lola                                                                #
#                                                                             #
###############################################################################

Vagrant.require_version ">= 1.6.0"
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "phusion/ubuntu-14.04-amd64"

  # Forwarding django port
  config.vm.network "forwarded_port", guest: 8000, host: 8000

  # IP address to access the django api
  config.vm.network "private_network", ip: "192.168.33.10"

  config.vm.provider "virtualbox" do |vb|
     vb.name = "Towan dev"
     vb.customize ["modifyvm", :id, "--memory", "2048"]
     vb.customize ["modifyvm", :id, "--nicpromisc2", "allow-all"]
  end

  config.vm.synced_folder ".", "/home/vagrant/workspace"

  # We now provision our Vitualbox with a docker postgres container
  # and a docker postgres data container.
  config.vm.provision "docker" do |d|
    # Postgres data container
    d.run "data",
      image: "postgres",
      args: "-v /data",
      cmd: "/bin/true"

    # Postgres container
    d.run "postgres",
      image: "postgres",
      args: "-p 5432:5432 --volumes-from data -e POSTGRES_PASSWORD=deadbeef"
  end

  # Install Django and load all the requirements
  # TODO: Provision with ansible ?
  config.vm.provision :shell, path: "provision.sh"

end
