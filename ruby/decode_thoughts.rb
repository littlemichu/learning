require 'optparse'
require 'ostruct'
require 'pp'

require_relative 'settings'

DIR_NAME = 'thoughts'
$stdout.sync = true

options = OpenStruct.new
options.file_names = []

# Create option parser 
opt_parser = OptionParser.new do |opts|
  opts.banner = "Usage: decode_thoughts.rb <file_name0> <file_name1> ..."
  opts.separator ""
  opts.separator "Specific options:"

  # --file option
  opts.on("-f", "--file FILENAME1[,FILENAME2,FILENAME3,...]", Array,
          "Print the decoded message(s) for the given file name(s)",
	  "Do NOT insert spaces between the commas") do |file_names|
    options.file_names = file_names
  end

  # --help option
  opts.on_tail("-h", "--help", "Show this message") do
    puts opts
    exit
  end
end

# Parse ARGV
opt_parser.parse!

# Takes the name of a file and returns the decoded contents of the file
# Params:
# +file_name+:: name of the file to decode
def decode(file_name)
  thought = ""

  # Open file and substitute the encoded words with the original word
  if File.file?(file_name)
    thought = File.read(file_name).downcase.reverse
    SharedVars::CODE_WORDS.each do |real, code|
      thought.gsub!(code, real)
    end
  end
  return thought
end

# Tries to return a valid path given a name. Returns nil otherwise
# Params:
# +name+:: name of a file
def get_valid_path(name)
  # Try just adding dir name in front
  path = DIR_NAME + "/" + name
  if File.file?(path) 
    return path 
  end

  # Try adding dir name, 'thought-' prefix and '.txt' extention
  path = DIR_NAME + "/thought-" + name + ".txt"
  if File.file?(path) 
    return path
  end

  # Return nil if unable to find a valid path
  return nil
end

# If no file names are given, prompt the user for a name of a thought
if options.file_names.empty?
  puts "\nDecode thought script -----------------------"
  sleep(1)
  puts "\nType \"Let me out\" or ^C to exit"
  input = ""

  # Continue asking for thoughts to decode until user decides to exit
  while true
    sleep(1)

    # Get name of thought from user
    print "\nPlease input the name of a thought to decode: " 
    input = $stdin.gets.strip
    file_name = DIR_NAME + "/thought-" + input + ".txt"
    sleep(1)

    # User wants to leave, exit program
    if input == "Let me out" 
      puts "\nHad enough already?\nWhat's the magic word~? (say \"pls\"): "
      if $stdin.gets.strip == "pls"
        sleep(2)
        puts "...fine. See you next time!"
	sleep(1)
	exit
      else
        sleep(1)
        puts "That's not the magic word..."
      end

    # If file exists for given thought, decode and print
    elsif File.file?(file_name) 
      print "Decoding thought"
      (1..3).each do 
	print "."
        sleep(1)
      end
      puts "\nThought decoded!"
      sleep(1)
      decoded_thought = decode(file_name)
      puts decoded_thought

    # If no file exists for the given thought, apologize to the user
    else 
      puts "Sorry, " + input + " is not a valid thought..."
    end
  end

# If file names are provided, decode and print each thought 
else
  valid_file_names = []
  invalid_file_names = []

  # Sort through file names: VALID or INVALID
  options.file_names.each do |file_name| 
    # If valid file name, append to list of valid file names
    if File.file?(file_name) 
      valid_file_names << file_name 

    # Otherwise, try fleshing out the path before checking
    else
      # If able to obtain a valid path to the given name, add to list of valid names
      path = get_valid_path(file_name)
      if path 
        valid_file_names << path 
	
      # If still nothing, add it to list of invalid file names
      else
        invalid_file_names << file_name
      end
    end
  end

  # Print decoded thoughts for valid file names
  unless valid_file_names.empty?
    valid_file_names.each do |name| 
      sleep(1)
      puts "\n" + name + ":"
      sleep(0.5)
      puts decode(name)
    end
  end

  # Print names of files that do not exist
  unless invalid_file_names.empty?
    puts "\nUnable to find matching files for these names: "
    invalid_file_names.each do |name|
      puts name
    end
  end
end 

