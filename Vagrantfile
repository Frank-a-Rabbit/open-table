Vagrant.configure("2") do |config|
  # Use the Rocky Linux Vagrant box
  config.vm.box = "trnc3/rockylinux-9"

  # Set up a private network
  config.vm.network "private_network", ip: "192.168.50.101"
  config.vm.synced_folder "D:/Projects/open_table", "/vagrant"

  # Define the provider-specific settings
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"  # Allocate 2GB of memory
    vb.cpus = 2         # Allocate 2 CPUs
  end

  # Set up a shell provisioner to update and install essential packages
  config.vm.provision "shell", inline: <<-SHELL
    sudo dnf update -y
    sudo dnf install -y vim git wget curl net-tools
  SHELL
end
