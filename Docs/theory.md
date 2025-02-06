### Software Design

Overall software design is concerned with the expandability, maintenance, reusability and testability.

Classes allow us to group related data and behaviour together. This makes it easier to read, understand and maintain the code. 
Furthermore, we can reuse code more efficiently, extend functionality without changing the original class due to
inheritance, and organise our code into more manageable units overall. One big file with only a few classes and extensive 
methods, however, will be challenging to navigate, modify as well as debug.

A complete lack of or even just sparse documentation in combination with an unstructured pile of code will, thus,  make it 
exceedingly difficult to gain an overview and manage the code in question. 

One of the fundamental software design principles which covers several issues with said unstructured pile of code is 
the SOLID Principle:
- Single responsibility - one class should only have one responsibility and only one reason to change
- Open/Closed - a class should be open for extension but closed for modification (existing code should not be changed)
- Liskov Substitution - a subclass should be able to replace its parent without changing the code
- Interface Segregation - a class should not have to implement irrelevant interfaces
- Dependency Inversion - high level moduls should not depend on low level moduls but rather abstractions

The KISS principle stands for 'Keep It Simple, Stupid' and literally means just that. Code should be as simple as possible
while still being effective, of course, and one should avoid unnecessary complexity and over-engineering wherever possible.

In conclusion, documentation, though often a pain in the a** to write, is essential for extensive projects. Especially
if they extend over longer periods of time and might not be handled by the same people from start to finish. Furthermore,
a clear structure with seperated clusters of related code will allow not only for a better reading and understanding but
also maintenance and debugging, thus making life easier for everyone involved.