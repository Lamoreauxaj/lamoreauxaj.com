---
navbar: false
sidebar: auto
---

# Welzl's Minimum Enclosing Circle Algorithm (Summer of Math Exposition)

## Introduction

One of my favorite algorithms is Welzl's minimum enclosing circle algorithm. I want to share this not only because it is elegant, but also because it highlights some great problem solving principles needed to discover it.

## Problem statement

The problem statement is as follows:

> Given $n$ points in the plane, find the circle with minimum radius which encloses all the points.

For example, this is the minimum enclosing circle for the following set of points.

![Figure. The minimum enclosing circle for the above points.](./media/images/main/Example_points_ManimCE_v0.8.0.png)

### Why does this matter?

Here are a few examples where this algorithm could be useful:

- Let's say you wanted to build a hospital and minimize the maximum distance to residents of a community; the minimum enclosing circle would give you a reasonable place to build such a hospital.
- Perhaps you want to approximate whether a point is close to any other point in a set. Naively, you could compare it to the other points in the set, however, a good approximation would be to first compare the distance to the minimum enclosing circle.
- Perhaps you want to approximate the maximum distance between two points in a set. In this case, the diameter of the minimum enclosing circle would be a good approximation.

But also if you're reading this, hopefully you would care about the problem solely for the interesting algorithm.

Maybe you have some ideas of how to start. I highly encourage you to take some time to mess around and see if you can come up with any ideas before reading ahead.

## Initial observations

Even though it may not be obvious how to solve this, a good problem solving strategy is to try to note any observations we can find in our initial investigation.

Perhaps after examining some examples, you ask yourself:

> How many points are on the boundary of the minimum enclosing circle?

Well we can first observe: if there were $0$ points on the boundary, then the circle could just be made smaller. For example, we could shrink the circle around the same center until at least one point is on the boundary of the circle.

![Figure. Shrinking circle until at least one point is on the boundary.](./media/videos/main/1080p60/No_boundary_points.mp4)

Since this would always result in a smaller circle as we can see above, this means that no minimum enclosing circle could have $0$ points on the boundary of the circle.

What if there were exactly one point on the boundary of the circle. Then we could shrink the circle around the single point as the origin until there is another point on the boundary of the circle.

![Figure. Shrinking circle until two points are on boundary.](./media/videos/main/1080p60/One_boundary_point.mp4)

So now we can conclude that there must be at least two points on the boundary of the minimum enclosing circle. But can there be exactly two points on the boundary? Well if we imagine shrinking the circle around the midpoint between the two fixed points, the circle would continue to get smaller until one of two things happen. Either the circle cannot get any smaller or a third point is now on the boundary of the circle.

For example, in the example we have been using, we can see that after doing this, the circle now has the two fixed points on the diameter of the circle.

![Figure. Shrinking circle until two points are on diameter of circl.](./media/videos/main/1080p60/Two_boundary_points.mp4)

The other case can be seen in the following example, where the circle ends up with three points on the boundary of the circle.

![Figure. Shrinking circle until three points are on boundary.](./media/videos/main/1080p60/Two_boundary_points_to_three.mp4)

### Naive algorithm

Thus far, we have concluded if the minimum enclosing circle has two points on the boundary, they are on the diameter of the circle. Otherwise there must be at least three points on the boundary of the circle. If there are more than three points, note that it only takes exactly three points to determine a circle. Thus if we are interested in trying all possible circles, we only need to worry about trying sets of at most $3$ points.

This gives us an algorithm: if we try all sets of $2$ to $3$ points and determine the circle that goes through them given the above conditions, we can take the circle of minimum radius which also encloses all other points. However this algorithm is pretty naive, but would be correct. When describing the runtime we would say this algorithm runs in $O(n^4)$ time. This is because there are $O(n^3)$ sets of points we have to try and for each one we have to check if all other $n$ points are within the circle.

Note, the notation $O(f(n))$ indicates that the runtime of the algorithm grows at most as fast as $f(n)$ grows. Thus when we say the algorithm is $O(n^4)$, it means it grows no faster than $n^4$, i.e. if we double the input, the runtime should at most be $16$ times larger. And we also assume this asymptotically, i.e. as $n$ goes to infinity this holds.

For this problem, we would hope we can get something much closer to $O(n)$. And in fact as we will see Welzl's algorithm does end up running in expected $O(n)$ time.

## The algorithm

### Wishful thinking

A good problem solving strategy when you don't know what to do is to simplify the problem by assuming you already know something you don't. For this problem, what if a little birdie already told you two of the points that would be on the boundary of the circle? How would you then find the minimum enclosing circle given this fact?

The idea is that we will keep track of a set of points and the current minimum enclosing circle for the set. At the start the set contains only the two fixed points and we know how to compute the smallest enclosing circle for this set. If we can keep this invariant (a property that doesn't change as we progress) as we add points then we will end up with the answer once the set contains all points.

We can consider a point not in the current set and whether it's within the current minimum enclosing circle or not. If it's within the circle, then the circle remains the same and we add the point to the set.

However if a point is not within the circle, then we can conclude that the point must actually be on the boundary of the minimum enclosing circle for the current set (since if it wasn't, it would've been in the current circle).

Thus at this point, we know three points that must be on the boundary of the circle. Therefore we can conclude that we in fact know the entire circle. Note the circle may not still enclose all points in the set, in which case there cannot exist any enclosing circle for this set, in which case the algorithm stops.

We can continue this process for each point. If we already have three points on the boundary and have a fourth point outside the circle, we use the original two fixed points along with the additional point. We no longer assume the previous point we added is on the boundary of the minimum enclosing circle.

The following animation shows this process on an example set of points.

![Figure. Finding minimum enclosing circle given two fixed points.](./media/videos/main/1080p60/Adding_points_from_two_fixed.mp4)

Now you may also wonder what the runtime of this algorithm is, but we will actually proceed and address that after we extend it to the full algorithm.

### One fixed point

The natural question to ask would be how to do this if you know less than two of the points which must be on the boundary. Optimally we would assume we know none of them, but what if we assumed that we know one point that must be on the boundary of the circle.

Similarly to when we assumed we know two points, whenever we encounter a point not within the current circle, we can assume we know that this point and the fixed point are on the boundary of the circle. However that isn't enough to determine the circle, but recall we have a routine to take two fixed points, and compute the minimum enclosing circle. Thus we can use the routine described above and now we can have the minimum enclosing circle of the set of points so far. If at any point, we conclude there does not exist any minimum enclosing circle, we can stop the algorithm.

We continue this process until we have the minimum enclosing circle of all the points given that one fixed point must be on the boundary. The following animation visualizes this routine.

![Figure. Finding minimum enclosing circle given two fixed points.](./media/videos/main/1080p60/Adding_points_from_one_fixed.mp4)

### The final routine

You probably can see where this is going, but can we just mirror the previous routine and assume we know zero points on the boundary of the circle?

If we add a point which is not within the current circle, we can use the previous routine in order to conclude the entire minimum enclosing circle for our current set of points. Thus by the end of this routine, we know we have the minimum enclosing circle for all points. The following is an animation of this routine.

![Figure. Finding minimum enclosing circle on all points.](./media/videos/main/1080p60/Adding_points_from_zero_fixed.mp4)

## Runtime

Now you've actually seen the entire algorithm. However what would you say the runtime of this algorithm is? A simple analysis would seem to suggest that we may have to run the recursive routine given an additional fixed point every time that we add a point. This would mean that the runtime given two fixed points would be $O(n^2)$, given one fixed point would be $O(n^3)$, and the total runtime would be $O(n^4)$. This is no better than the naive algorithm.

However I claim that if you shuffle the points randomly, then on average this algorithm runs in $O(n)$ time. Let's consider the case where we have two fixed points. We want to know the total amount of work done which is $O(n)$ times the number of times we have to recompute the circle. However if we take the points in a random order, how often does this happen? It's probably not obvious, however if we take a different perspective and consider that we are removing the points it becomes clearer.

Everytime you remove a point, the probability that you shrink the circle is only if you remove a point which is on the boundary of the circle. This is $\frac{3}{n}$ points. Therefore the expected number of times the circle shrinks is expected $O(1)$ which is the same as the number of times the circle would have expanded in our algorithm. Since every time you expand the circle, you have to do $O(n)$ work, the total runtime ends up being $O(n)$.

The same logic applies for when we have one fixed point, we only expect the circle to expand on average $O(1)$ times and therefore the total work done is $O(n)$. You can probably see that when we have no fixed points, the total runtime ends up being $O(n)$.

So just by randomizing the order we process the points in, suddenly our worst case runtime actually beceomes very unlikely since it's rare adding a point will expand the circle. Thus not only is this algorithm correct, it is very efficient.

## Implementation

If you are curious on what the implementation of this algorithm would look like, hopefully the following code gives you an idea. As we loop over the points, we check if they are not in the circle and run the routine with one more fixed point on the current set of points. We keep track of the set of points, by just running the routine over a prefix of the array `points` which is controled by `current_prefix_len`.

```python
def mec(points, fixed_points, current_prefix_len):
    # compute starting circle
    current_circle = circle_from_fixed_points(fixed_points)
    for i in range(current_prefix_len):
        # check if new point is not in circle
        if not point_in_circle(points[i], current_circle):
            if len(fixed_points) == 3: # no circle exists
                return None
            # update circle by running with one more fixed point
            current_circle = mec(points, fixed_points + [points[i]], i + 1)
            if current_circle is None: # no circle exists
                break
    return current_circle
```

## Conclusion

That's the entire algorithm. I hope you feel that you could have discovered this algorithm. It's a great example of what wishful thinking and just investigating the results can do.

<style lang="stylus">
img
    border-radius: 6px
figcaption
    color: #999
blockquote
    color: #2c3e50
video
    width: 100%
    border-radius: 6px
</style>

