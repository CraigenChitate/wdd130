import './blog-post.js';
import './blog-post-list.js';

const blogPostsElement = document.getElementById('blog-posts');

blogPostsElement.posts = [
  {
    title: 'How to become a web developer in 6 months',
    description: 'Learn the skills you need in web development and get a job within 6 months'
  },
  {
    title: 'Web Components will enhance Javascript libraries, not replace them',
    description: 'Learn Javascipt and understand how you can implete javascript in real world'
  },
  {
    title: 'How to properly build web components to help you scale easily',
    description: 'Learn how you can create your own web components and how you can reuse them again.!'
  },
  {
    title: 'How to build a fullstack website start to finish',
    description: 'Learn to build your websites from beginning to end.'
  },
  {
    title: 'NodeJs projects that will make you a full stack',
    description: 'Learn NodeJs and understand how you can create your own full stack projects.!'
  },
  {
    title: '10 CSS tricks you need to learn for your next project',
    description: 'Learn CSS and become a pro.'
  }
]