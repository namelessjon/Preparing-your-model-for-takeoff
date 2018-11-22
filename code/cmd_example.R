# cmd_example.R
# shows how to use command line arguments

doc <- "Usage: cmd_example.R [options] [--] <input_data> <input_model> <output_classification>

Example:
  Rscript cmd_example.R iris.csv iris.rds predictions.csv

Options:
-h, --help             this help
-l LEVEL, --log LEVEL  logging level [default: INFO]
"
(args <- docopt::docopt(doc))
#> List of 12
#>  $ --help                 : logi FALSE
#>  $ --log                  : chr "INFO"
#>  $ --                     : logi FALSE
#>  $ <input_data>           : chr "iris.csv"
#>  $ <input_model>          : chr "iris.rds"
#>  $ <output_classification>: chr "predictions.csv"
#>  $ help                   : logi FALSE
#>  $ log                    : chr "INFO"
#>  $                        : logi FALSE
#>  $ input_data             : chr "iris.csv"
#>  $ input_model            : chr "iris.rds"
#>  $ output_classification  : chr "predictions.csv"
print(args$input_data)
#> "iris.csv"

# Do things with the arguments
# ...
  
  
