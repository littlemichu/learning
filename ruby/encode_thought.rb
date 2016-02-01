require_relative "settings"
$stdout.sync = true

# Get text and swap in code words
puts "Enter your thought:"
thought = gets.downcase
SharedVars::CODE_WORDS.each do |real, code|
  thought.gsub!( real, code )
end

# Save the jibberish to a new file
puts "File encoded. Please enter a name for this thought:"
idea_name = gets.strip
File::open( "thought-" + idea_name + ".txt", "w") do |f|
  f << thought.upcase.reverse
end
