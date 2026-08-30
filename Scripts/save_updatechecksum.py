import sys
import struct
import argparse

def update_checksum(file_path, file_type):
    try:
        with open(file_path, 'r+b') as f:
            data = f.read()
            file_size = len(data)

            # read old checksum
            old_checksum = struct.unpack('<I', data[:4])[0]

            # compute checksum over bytes from offset 0xC to end
            checksum_bytes = data[0xC:]

            if file_type == 'slot':
                # 8-bit checksum
                new_checksum = sum(checksum_bytes) & 0xFF
            else:  # 'system'
                # 32-bit checksum
                new_checksum = sum(checksum_bytes) & 0xFFFFFFFF

            print(f"Old Checksum: 0x{old_checksum:08X}")
            print(f"New Checksum: 0x{new_checksum:08X}")

            # write the new checksum
            f.seek(0)
            f.write(struct.pack('<I', new_checksum))

        print("Checksum updated successfully.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Update checksum of a save file or system file."
    )
    parser.add_argument("file", help="Path to the input file")
    parser.add_argument(
        "-t", "--type",
        choices=['slot', 'system'],
        default='slot',
        help="File type: 'slot' (8-bit checksum) or 'system' (32-bit checksum). Default: slot"
    )
    args = parser.parse_args()
    update_checksum(args.file, args.type)
