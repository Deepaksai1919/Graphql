const { ApolloServer } = require('apollo-server');
const { PrismaClient } = require('@prisma/client')
const fs = require('fs');
const typeDefs = fs.readFileSync('schema/types.graphql', 'utf-8');
const { getUserId } = require('./utils');
const Query = require('./resolvers/Query');
const Mutation = require('./resolvers/Mutation');
const User = require('./resolvers/User');
const Link = require('./resolvers/Link');

const prisma = new PrismaClient();
const resolvers = {
  Query,
  Mutation,
  User,
  Link
}

const server = new ApolloServer({
  typeDefs,
  resolvers,
  context:({ req }) => {
    return {
      ...req,
      prisma,
      userId: req && req.headers.authorization ? getUserId(req) : null
    }
    req,
    prisma
  }
})

server
  .listen()
  .then(({ url }) =>
    console.log(`Server is running on ${url}`)
  );
