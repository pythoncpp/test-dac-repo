const express = require('express')
const router = express.Router()

router.post('/signin', (request, response) => {
  response.send('done')
})

module.exports = router
