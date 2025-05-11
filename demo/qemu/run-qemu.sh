qemu-system-arm \
  -kernel qemu-rpi/kernel-qemu-4.19.50-buster \
  -cpu arm1176 \
  -m 256 \
  -M versatilepb \
  -dtb qemu-rpi/versatile-pb.dtb \
  -no-reboot \
  -serial stdio \
  -append "root=/dev/sda2 rootfstype=ext4 rw console=ttyAMA0 init=/bin/sh"  \
  -hda 2024-11-19-raspios-bookworm-armhf-lite.img
