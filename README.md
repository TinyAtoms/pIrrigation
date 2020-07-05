# TODOs  
- [ ] Sagar: Make function to chart past water expenditure, ET, crop factor  
- [ ] GROUP: Rethink the plantgroup.water_now function.  



# Finished
- [X] Django server
- [X] Crop factor for a given day and crop
- [X] Make past group water expenditure data  
- [X] plant data as model  
- [X] GROUP: Rethink float valve idea   
- [X] Detailview with editor  
- [X] Make python script to schedule crop jobs to water and to measure 
- [X]  Determine pan factor function   

# HOW TO RUN THIS:
so you do a `manage.py runserver`, and you schedule `python manage.py process_tasks -duration=300` to be run every 5 mins, in cron or in windows task scheduler