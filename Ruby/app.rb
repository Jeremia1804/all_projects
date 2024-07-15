require 'sinatra'

get '/' do
  "Hello, world!"
end

get '/about' do
    str = "jeremia"
  "This is a simple Sinatra application."
  return str
end

get '/hello/:name' do
  "Hello, #{params['name']}!"
end
