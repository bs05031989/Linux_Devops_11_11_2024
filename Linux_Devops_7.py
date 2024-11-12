"""
lsblk : list the attached blocks of volume /dev/xvda
df -h : Storage 
mount point : / bind with a location

AWS : Elastic Block Store (EBS)

sdf 
Attaching is not mounting

Physical Volume : Volume Group combines volumes (a,b,c)

Logical Volume : Any partition from total physical volume

Logical Volume Manager : Handles volume oriented things
 1. Attach disk 
 2. Create Physical Volumes
 go to lvm
 pvcreate /dev/xvdf /dev/xvdg /dev/xvdh

 Pvs : to see physical volume

 vgcreate : To create volume group
  
vgcreate bs_vg /dev/xvdf /dev/xvdg

vgs : volume group show

lvcreate -L 10G -n bs_lv  bs_vg : To crate logical volume out of created Volume group 

pvdisplay
lvdisplay

To mount logical volume

mkdir /mnt/bs_lv_mount
 Format the logical volume first using mkfs.ext4 /dev/bs_vg/bs_lv
 mount /dev/bs_vg/bs_lv  /mnt/bs_lv_mount

If direct disk mounting 

mkfs -t ext4 /dev/xvdh

To extend Logical volume

lvextend -L +5G /dev/bs_vg/bs_lv



"""