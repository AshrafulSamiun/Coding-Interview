# Read input values
n, m = map(int, input().split())  # Number of posts and queries
likes = list(map(int, input().split()))  # Initial likes on posts

# Process each query
for _ in range(m):
    post_no, like_increase = map(int, input().split())
    likes[post_no - 1] += like_increase  # Update the likes for the given post

    # Find the post with the highest likes (smallest index in case of tie)
    max_likes = max(likes)
    best_post = likes.index(max_likes) + 1  # Convert 0-based index to 1-based

    # Print the result
    print(best_post, max_likes)
