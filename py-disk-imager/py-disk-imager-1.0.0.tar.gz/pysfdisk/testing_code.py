# pylint: skip-file
# flake8: noqa

from block_device import BlockDevice

# import getdevinfo

if __name__ == "__main__":
    disk = BlockDevice(path="/dev/sdc", use_sudo=True)
    # with open("disk_partition_dump", "w") as dump_file:
    #     dump_file.write(disk.dump_partition_table())
    #
    # disk.dump_mbr(destination_file="mbr_file")
    # disk.dump_partition_table()
    # disk.dump_partitions()
    # print(disk.compress_dumped_partitions(target_dir="/home/tom/Desktop"))
    print(disk.run(mbr_filename="mbr_file", target_dir="/home/tom/Desktop"))
