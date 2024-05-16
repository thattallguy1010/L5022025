import napalm
import sys
import os

config_file = "configs/borderleaf1.cfg"

driver = napalm.get_network_driver("eos")
device = driver(
    hostname="borderleaf1",
    username="automator",
    password="arista123",
    # key_file="~/.ssh/id_pub",
    # optional_args={"use_keys": True},
)

print("Opening ...")
device.open()

print("Loading replacement candidate ...")
device.load_replace_candidate(filename=config_file)


print("\nDiff:")
print(device.compare_config())


# device.commit_config()
# else:
#     print("Discarding ...")
#     device.discard_config()

# # close the session with the device.
device.close()
print("Done.")

