require 'sinatra'
require './affichage/Affichage.rb'

get '/' do
  "Hello, world!"
end

get '/about' do
  con = MyConnection.connect()
  tab = [1]
  @check = Affichage.afficherCheck(con)
  @table = Affichage.afficherRNPrest(con,tab)
  con.close()
  erb :index
end

get '/checker' do
  con = MyConnection.connect()
  nb = Affichage.nbLalana(con)
  tab = []
  a = 0
  for i in 0...nb
    if(params[i.to_s]!=nil)
      tab.push(params[i.to_s].to_i)
    end
  end
  puts tab
  @check = Affichage.afficherCheck(con)
  @table = Affichage.afficherRNPrest(con,tab)
  con.close()
  erb :index
end

get '/change' do
  id = params['id']
  fo = params['fo']
  con = MyConnection.connect()
  Affichage.changeFormule(con,id,fo)
  con.close()
  redirect '/about'
end

get '/hello/:name' do
  "Hello, #{params['name']}!"
end

get '/test' do
  "nety le izy ee"
end