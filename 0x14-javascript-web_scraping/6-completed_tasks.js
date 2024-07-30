#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.log(`Error: ${response.statusCode}`);
    return;
  }

  const tasks = JSON.parse(body);
  const userTasks = {};

  // Count completed tasks per user
  tasks.forEach(task => {
    if (task.completed) {
      if (!userTasks[task.userId]) {
        userTasks[task.userId] = 0;
      }
      userTasks[task.userId]++;
    }
  });

  // Print the results in object literal format
  console.log(userTasks);
});
