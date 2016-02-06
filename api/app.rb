#
# weather-app-tutorial
# A Weather API
# v0.0.1
#

# See: http://gembundler.com/bundler_setup.html
#      http://stackoverflow.com/questions/7243486/why-do-you-need-require-bundler-setup
ENV['BUNDLE_GEMFILE'] ||= File.expand_path('../../Gemfile', __FILE__)

require 'bundler/setup' if File.exists?(ENV['BUNDLE_GEMFILE'])

require 'sinatra'
require 'json'
require 'rest_client'

get '/' do
  content_type :json
  { message: 'Hello World!' }.to_json
end

not_found do
  content_type :json
  halt 404, { error: 'URL not found' }.to_json
end
