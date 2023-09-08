#!/bin/bash

if [ $# -ne 1 ]; then
	    echo "Usage: $0 <path>"
	        exit 1
fi

input_path="$1"
output_dir="$input_path/../output"

if [ ! -d "$output_dir" ]; then
	    mkdir "$output_dir"
	        echo "Created output directory: $output_dir"
fi

cd "$input_path" || exit 2

for file in *.*; do
	    filename="${file%.*}"
	        extension="${file##*.}"

		    if [[ "$filename" =~ ^[0-9]+$ ]]; then
			            new_name=$(printf "%05d" "$filename")
				            new_filename="$new_name.$extension"
					            cp "$file" "$output_dir/$new_filename"
						            echo "Moved $file to $output_dir/$new_filename"
							        fi
							done

							echo "File renaming and moving completed."

