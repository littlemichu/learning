require_relative "settings"

$stdout.sync = true
dirname = 'thoughts'

# Get text and swap in code words
puts "Enter your thought:"
thought = gets.downcase
SharedVars::CODE_WORDS.each do |real, code|
  thought.gsub!( real, code )
end

# Create directory to store thoughts in if it doesn't exist
Dir.mkdir(dirname) unless Dir.exists?(dirname) 

# Get a name for the thought
print "\nThought encoded. Please enter a name for this thought: "
thought_name = gets.strip
while File.exist?(dirname + '/thought-' + thought_name + '.txt') do
  puts "Sorry, that name has already been used."
  print "\nPlease enter another name for your thought: "
  thought_name = gets.strip
end

# Save the jibberish to a new file
File::open( "thoughts/thought-" + thought_name + ".txt", "w") do |f|
  f << thought.upcase.reverse
end

puts "\n'" + thought_name + "' thought saved."
puts "Thanks for your thought!"

