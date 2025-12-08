This project is a Flight Booking Simulator built using FastAPI and SQLite.Milestone 1 focuses on the Core Flight Search & Data Management module.
The goal of Milestone 1 is to create the core backend system that can store flight details and allow users to search for flights based on different filters.In this milestone, I designed a clean database structure for storing flight information such as origin, destination, departure time, arrival time, base fare, seats, status, and airline details. I also created a set of API endpoints that allow users to view all flights and search based on origin, destination, date, or sorting preferences like price, duration, or departure time.

The backend is built using FastAPI because it is modern, fast, and simple to integrate. SQLite was used for this milestone as it’s lightweight and easy to manage during development. SQLAlchemy was used for ORM so the database tables and models are neatly organized.The APIs are organized inside a dedicated router, and Swagger documentation is automatically available at /docs, where all endpoints can be tested directly.This milestone focuses only on core data management and search functionality. Upcoming milestones will include dynamic pricing, booking workflow, concurrency handling, and frontend integration.

Overall,this provides Milestone 1 as this backend will serve as the foundation for upcoming milestones like dynamic pricing, booking workflow, concurrency handling, and UI integration.
To run the project locally, install dependencies, initialize the database, and start the FastAPI server using Uvicorn.
You can then open http://127.0.0.1:8000/docs to explore and test all the APIs.

After completing the basic flight search system in Milestone 1, Milestone 2 focuses on adding real-world dynamic features to make the system behave like an actual airline backend. In this milestone, I implemented a dynamic pricing engine that automatically adjusts the ticket price based on factors like remaining seats, time left for departure, and simulated demand levels. I also created a demand simulator to randomly generate HIGH, MEDIUM, or LOW demand so that every search result feels realistic.

The search API was upgraded to support more filters such as airline, travel class, and flight status, along with pagination for better data handling. Every time a user searches, the price shown is dynamically updated using the new pricing logic. I also added a small simulated external API that returns live-style airline status such as delays or cancellations.

Overall, Milestone 2 enhances the backend by adding intelligent pricing, better filtering, and more realistic behavior, preparing the system for the next stage where users will be able to book flights, manage seats, and handle concurrency.
