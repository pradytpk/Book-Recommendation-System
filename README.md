# Books Recommendation System Based on Clusterting & Collaborative

### What is recommendation System

- A recommendation system, also known as a recommender system or a recommendation engine, is a software application or algorithm designed to provide personalized suggestions or recommendations to users.
- These recommendations are typically related to products, services, content, or items that users might be interested in, based on their preferences, past behavior, or the behavior of similar users.
- Recommendation systems are widely used in various domains, including e-commerce, content streaming, social media, and more, to enhance user experiences, increase engagement, and drive sales or interactions.

#### Types of recommendation system

1. **Content based**
   - Content-based recommendation systems recommend items to users based on the characteristics and attributes of those items and the user's preferences.
   - It involves analyzing the content or features of items and creating user profiles based on their past interactions or explicitly provided preferences.
   - Recommendations are made by matching the content of items with the user profile to find items that align with the user's interests.
2. **Collaborative filtering based**
   - Collaborative filtering recommendation systems make recommendations by leveraging the behavior and preferences of a large number of users.
   - There are two main types of collaborative filtering: user-based and item-based.
     a. **User-based** collaborative filtering recommends items to a user based on the preferences and behavior of users who are similar to that user.
     b. **Item-based** collaborative filtering recommends items to a user based on the similarity between items they have interacted with and those recommended items.
   - Collaborative filtering can be further divided into **memory-based** and **model-based** approaches.
3. **Hybrid based**
   - Hybrid recommendation systems combine multiple recommendation techniques to provide more accurate and diverse recommendations.
   - By combining content-based and collaborative filtering approaches, hybrid systems can overcome the limitations of each individual method.
   - Hybrid systems can be implemented in various ways, such as using a weighted combination of recommendations from different methods or by using one method to improve or filter recommendations from another method.

```
conda create --prefix ./env python== 3.11.5 -y
```

```
conda activate ./env/
```
