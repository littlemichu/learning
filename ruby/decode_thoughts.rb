require 'optparse'
require 'ostruct'
require 'pp'

require_relative 'settings'

$stdout.sync = true

options = OpenStruct.new
options.filenames = []

# Create option parser 
opt_parser = OptionParser.new do |opts|
  opts.banner = "Usage: decode_thoughts.rb <filename0> <filename1> ..."
  opts.separator ""
  opts.separator "Specific options:"

  # --file option
  opts.on("-f", "--file FILENAME1[, FILENAME2, FILENAME3, ...]", Array,
          "Print the decoded message(s) for the given filename(s)") do |filenames|
    options.filenames = filenames
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
# +filename+:: name of the file to decode
def decode(filename)
  thought = ""

  # Open file and substitute the encoded words with the original word
  if File.file?(filename)
    thought = File.read(filename).downcase.reverse
    SharedVars::CODE_WORDS.each do |real, code|
      thought.gsub!(code, real)
    end
  end
  return thought
end

# If no filenames are given, prompt the user for a name of a thought
if options.filenames.empty?
  puts "\nDecode thought script -----------------------"
  sleep(1)
  puts "\nType \"Let me out\" or ^C to exit"
  input = ""

  # Continue asking for thoughts to decode until user decides to exit
  while true
    sleep(1)

    # Get name of thought from user
    print "\nPlease input the name of a thought to decode: " 
    input = gets.strip
    filename = "thoughts/thought-" + input + ".txt"
    sleep(1)

    # User wants to leave, exit program
    if input == "Let me out" 
      puts "\nHad enough already?\nWhat's the magic word~? (say \"pls\"): "
      if gets.strip == "pls"
        sleep(3)
        puts "...fine. See you next time!"
	sleep(1)
	exit
      else
        sleep(1)
        puts "That's not the magic word..."
      end

    # If file exists for given thought, decode and print
    elsif File.file?(filename) 
      print "Decoding thought"
      (1..3).each do 
	print "."
        sleep(1)
      end
      puts "\nThought decoded!"
      sleep(0.5)
      decoded_thought = decode(filename)
      puts decoded_thought

    # If no file exists for the given thought, apologize to the user
    else 
      puts "Sorry, " + input + " is not a valid thought..."
    end
  end

# If filenames are provided, decode and print each thought 
else
  filenames = []
  invalid_filenames = []
  options.filenames.each do |filename| 
    if File.file?(filename) 
      filenames << filename 
    else
      invalid_filenames << filename
    end
  end

  # Print names of files that exist
  unless filenames.empty?
    puts "\nThese files exist: "
    filenames.each do |name| 
      puts name 
    end
  end

  # Print names of files that do not exist
  unless invalid_filenames.empty?
    puts "\nThese files do not exist: "
    invalid_filenames.each do |name|
      puts name
    end
  end
end 

