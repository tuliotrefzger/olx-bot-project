#!/bin/bash

# Read HTML content from standard input
html_content=$(cat)

# Use grep to extract lines containing "option" tags, then use sed to extract the label attribute values
labels=$(echo "$html_content" | grep -oP 'label="\K[^"]+' | sed 's/\&amp;/\&/g')

# Convert the labels into an array
IFS=$'\n' read -d '' -r -a labels_array <<<"$labels"

# Remove the first two elements from the array
labels_array=("${labels_array[@]:2}")

# Convert the array to JSON format
json_array=$(printf '%s\n' "${labels_array[@]}" | jq -R . | jq -s .)

# Print the JSON array
echo "$json_array"
