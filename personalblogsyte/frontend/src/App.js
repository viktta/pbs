import React, { Component } from "react";

const list = [
  {
    id: 1,
    post: "First Post",
    author: "Admin",
    blog_date: "2020-01-21T01:00:00Z"
  },
  {
    id: 2,
    post: "Second Post",
    author: "Admin",
    blog_date: "2020-01-21T01:01:00Z"
  },
  {
    id: 3,
    post: "Third Post",
    author: "Admin",
    blog_date: "2020-01-21T01:02:00Z"
  }
];

class App extends Component {
  state = {
    todos: []
  };

  async componentDidMount() {
    try {
      const res = await fetch("http://127.0.0.1:8000/api/");
      const todos = await res.json();
      this.setState({
        todos
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div>
        {this.state.todos.map(item => (
          <div key={item.id}>
            <h1>{item.post}</h1>
            <p>{item.author}</p>
            <p>{item.blog_date}</p>
          </div>
        ))}
      </div>
    );
  }
}

export default App;
