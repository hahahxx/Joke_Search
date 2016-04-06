// Task component - represents a single todo item
Joke = React.createClass({
  propTypes: {
    // This component gets the joke to display through a React prop.
    // We can use propTypes to indicate it is required
    joke: React.PropTypes.object.isRequired
  },
  render() {
    console.log(this.props.data);
    return (
      <li>{this.props.joke._source.content}</li>
    );
  }
});
