require 'pg'

class MyConnection
    def self.connect()
        # Initialize connection variables.
        host = String('localhost')
        database = String('lalanaruby')
        user = String('postgres')
        password = String('postgres')

        # Initialize connection object.
        connection = PG::Connection.new(:host => host, :user => user, :dbname => database, :port => '5432', :password => password)

    return connection
    end
end

