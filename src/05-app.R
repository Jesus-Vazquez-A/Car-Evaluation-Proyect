library(shiny)
library(caret)
library(randomForest)




# load model
model<-readRDS("model.RDS") 

ui <- pageWithSidebar(
  
  # Page header
  headerPanel('Car Evaluation'),
  
  # Input values
  sidebarPanel(
    HTML("<h3>Input parameters</h4>"),
    
    
    
    sliderInput("buying","Buying (0-3)",min = 0,max = 3,step = 1,value = 2),
    
    sliderInput("maint","Maint (0-3)",min = 0,max = 3,step = 1,value = 1),
    
    selectInput("doors","Number of doors",choices = c(2,3,4,'More'),selected = 4),
    
    selectInput("persons","Number of persons",choices = c(2,5,'More'),selected = 5),
    
    sliderInput("lug_boot","Lug Boot (0-2)",min = 0,max = 2,step = 1,value = 0),
    
    sliderInput("safety","Safety (0-2)",min = 0,max = 2,step = 1,value = 0),
    

    
    actionButton("submitbutton", "Submit", class = "btn btn-primary")
  ),
  
  mainPanel(
    tags$label(h3('Status/Output')), # Status/Output Text Box
    verbatimTextOutput('contents'),
    tableOutput('tabledata') # Prediction results table
    
  )
)

####################################
# Server                           #
####################################

server<- function(input, output, session) {
  
  
  
  # Input Data
  
  datasetInput <- reactive({  
    
    buying<-input$buying
    maint<-input$maint
    doors<-input$doors
    persons<-input$persons
    lug_boot<-input$lug_boot
    safety<-input$safety
    
    
    doors = ifelse(doors == 'More',5,doors)
    doors = as.numeric(doors)
    
    persons = ifelse(persons == 'More',5,doors)
    persons = as.numeric(persons)
    
  #  Transform character type variables to numeric type, 
  #  since R when seeing a string type element standardizes the variable transforms it to character type
    
    
    
    newdata<-data.frame(buying,
                        maint,doors,
                        persons,lug_boot,
                        safety)
    
    pred = predict(model,newdata)
    
    print(paste("Purchase Recommendation: ",pred)) 
    

    
  })
  
  # Status/Output Text Box
  output$contents <- renderPrint({
    if (input$submitbutton>0) { 
      isolate("Calculation complete.") 
    } else {
      return("Server is ready for calculation.")
    }
  })
  
  # Prediction results table
  output$tabledata <- renderTable({
    if (input$submitbutton>0) { 
      isolate(datasetInput()) 
    } 
  })
  
}

####################################
# Create the shiny app             #
####################################
shinyApp(ui = ui, server = server)