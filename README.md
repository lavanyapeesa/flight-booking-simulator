This project is a Flight Booking Simulator built using FastAPI and SQLite.
The goal of Milestone 1 is to create the core backend system that can store flight details and allow users to search for flights based on different filters.

In this milestone, I designed a clean database structure for storing flight information such as origin, destination, departure time, arrival time, base fare, seats, status, and airline details. I also created a set of API endpoints that allow users to view all flights and search based on origin, destination, date, or sorting preferences like price, duration, or departure time.

The backend is built using FastAPI because it is modern, fast, and simple to integrate. SQLite was used for this milestone as it’s lightweight and easy to manage during development. SQLAlchemy was used for ORM so the database tables and models are neatly organized.

The APIs are organized inside a dedicated router, and Swagger documentation is automatically available at /docs, where all endpoints can be tested directly.

This milestone focuses only on core data management and search functionality. Upcoming milestones will include dynamic pricing, booking workflow, concurrency handling, and frontend integration.

Overall,this provides Milestone 1 
