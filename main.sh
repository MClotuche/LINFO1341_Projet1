#!/bin/bash

# Check if an argument is provided
if [ $# -eq 0 ]; then
    echo "Error: Please provide a name for the capture and SSL log file."
    exit 1
fi

name="$1"
capture_file_bg="captures/raw_bg/${name}_bg_capture.pcap"
capture_file_chrome="captures/raw_chrome/${name}_chrome_capture.pcap"
ssl_log_file="keys/${name}_log.txt"

# Step 1: Start network analysis with tcpdump and save to a file (background noises)
sudo tcpdump -U -i any -w "$capture_file_bg" &
tcpdump_bg_pid=$!
echo "Capturing background noises for 10 seconds..."
sleep 10

# Step 2: Execute the command with SSLKEYLOGFILE and launch Google Chrome
SSLKEYLOGFILE="$ssl_log_file" google-chrome uclouvain-my.sharepoint.com &
chrome_pid=$!
echo "Chrome launched..."

# Step 3: Start network analysis with tcpdump and save to a file (Chrome)
sudo tcpdump -U -i any -w "$capture_file_chrome" &
tcpdump_chrome_pid=$!
echo "Capturing Chrome traffic..."

# Step 4: Wait for Chrome to close
wait $chrome_pid
echo "Chrome closed."

# Step 5: End the network analysis for Chrome
sleep 5
kill $tcpdump_chrome_pid
echo "Chrome capture finished."

sleep 5
# Step 7: End the network analysis for background noises
kill $tcpdump_bg_pid
echo "Background noises capture finished."

# Step 6: Filter background noises from Chrome capture: TODO
# Extract unique IP addresses, hosts, interfaces, source, and destination addresses from the background capture file
#unique_info=$(tcpdump -nnr "$capture_file_bg" | awk '{print $3}' | sort -u)

# Generate filter expression to exclude IP addresses, hosts, interfaces, source, and destination addresses
#filter_expression="not ("

# Add each unique item to the filter expression
#for item in $unique_info; do
#    filter_expression+="host $item or "
#done

# Remove the trailing "or" and close the parentheses
#filter_expression="${filter_expression%or } )"

#echo "Generated filter expression for background noises:"
#echo "$filter_expression"

# Apply the filter to the Chrome capture file
#sudo tcpdump -r "$capture_file_chrome" -w filtered_chrome.pcap "$filter_expression"

#echo "Background noises filtered out from Chrome capture."

# Step 8: Optionally generate SSL key log file
touch "$ssl_log_file"
echo "SSL key log file generated: $ssl_log_file"
