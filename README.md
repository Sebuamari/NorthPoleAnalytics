# Santa's Workshop Project

This Django project helps Santa manage the Christmas toy delivery process, calculate production time, and generate statistics based on the kids' gift wishes, niceness, and delivery requirements.

## Endpoints

### 1. `/admin/`

- **Method**: `GET`
- **Description**: Access the Django admin panel to manage models, including `Kid`, `Toy`, and `SantasList`.

- ### 2. `/statistics/`

- **Method**: `GET`
- **Description**: This endpoint returns statistics about Santa's lists. It includes name of the list and number of nice/naughty kids in that particular list.
  
  **Response:**
  ```json
  {
    "lists": [
      {
        "list_name": "Christmas 2024",
        "nice_kids_count": 17,
        "naughty_kids_count": 13
      }
    ]
  }

### 3. `/statistics/toys/`

- **Method**: `GET`
- **Description**: This endpoint returns statistics about the toys needed based on kids' gift wishes and their niceness. It includes the overall production time, toy count, and delivery time.
  
  **Response:**
  ```json
  {
    "toys_needed": [
      {
        "name": "Teddy Bear",
        "required_quantity": 2,
        "total_production_time": 10
      }
    ],
    "overall_production_time": 10,
    "overall_toy_count": 2,
    "naughty_kids_count": 1,
    "total_delivery_time": 4.5,
    "total_needed_time": 14.5
  }
