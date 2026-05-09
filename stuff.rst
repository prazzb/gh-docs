Stuff
#####

.. contents:: Table of contents
   :local:
   :backlinks: entry
   :depth: 2

WSL-Arch
********

This is to install arch on wsl for nix usage. Basic data from `here <https://wiki.archlinux.org/title/Install_Arch_Linux_on_WSL>`__
from archwiki. Also `wsl-config <https://learn.microsoft.com/en-us/windows/wsl/wsl-config>`__ from M$ website.

Set the following in /etc/wsl.conf as explained above

* automount.enabled to true
* interop.enabled to true
* interop.appendWindowPath is false
* boot.systemd is true

To install, run below on cmd

.. code-block:: shell

   wsl --install archlinux

It leaves at a root prompt. Add a user(userName here) and give root password.

.. code-block:: shell

   useradd -m userName
   passwd root
   vi /etc/wsl.conf # update above things
   exit

Do this in wsl to (default) login as user (hence no need for user password)

.. code-block:: shell

   wsl --manage archlinux --set-default-user userName

To login into arch, do as below

.. code-block:: shell

   wsl ~ -d archlinux

After logging in, do the following

.. code-block:: shell

   # things mentioned in the arch wiki page above
   # as root
   pacman -Syu xdg-utils mesa vulkan-dzn
   # as user
   echo "export GALLIUM_DRIVER=d3d12" >> ~/.bashrc
   echo "export LIBVA_DRIVER_NAME=d3d12" >> ~/.bashrc
   # personal list of packages, as root
   pacman -Syu neovim nix direnv

Enable en_US.UTF-8 in /etc/locale.gen as explained `here <https://wiki.archlinux.org/title/Locale>`__, add/edit to
/etc/locale.conf again as explained, and then run locale-gen as root.

For direnv, add hook as defined `here <https://direnv.net/docs/hook.html>`__, then do (after nix develop and have 
nix-direnv in the packages list)

.. code-block:: shell

   echo "use flake" >> .envrc && direnv allow

Nix
***

Some notes on installing nix for single user systems.

Do the following as root, where (userName is the user)

.. code-block:: shell

   mkdir /nix
   chown userName /nix
