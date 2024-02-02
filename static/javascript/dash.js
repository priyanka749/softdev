
const express = require('express');
const path = require('path');

const app = express();

// Serve static files from the 'template' directory
app.use('/template', express.static(path.join(__dirname, 'template')));

// Route for '/template/dash/'
app.get('/template/dash.html/', (req, res) => {
  res.sendFile(path.join(__dirname, 'template', 'dash', 'index.html'));
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
