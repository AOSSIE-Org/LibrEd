FROM node:24-slim

WORKDIR /app

# COPY package.json package-lock.json ./

COPY . .

RUN npm install

CMD ["npm", "run", "dev", "--", "--host"]
# CMD ["sh", "-c", "npm run build && npm run preview -- --host"]
