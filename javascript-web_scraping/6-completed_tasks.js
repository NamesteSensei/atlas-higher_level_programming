#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  try {
    const todos = JSON.parse(body);
    const completedTasks = {};

    todos.forEach((task) => {
      if (task.completed) {
        if (!completedTasks[task.userId]) {
          completedTasks[task.userId] = 0;
        }
        completedTasks[task.userId] += 1;
      }
    });

    console.log(completedTasks);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
