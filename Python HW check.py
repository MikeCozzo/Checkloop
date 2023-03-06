# This program displays the total of the
# amounts in the sales_data.txt file.

def main():
    total = 0.0
    
    try:
        infile = open('sales_data_with_junk.txt', 'r')

        for line in infile:
            try:
                amount = float(line)
            except ValueError:
                line = line.strip('\n')
                print('Non-numeric data found in the file:'+line)    
            else:
                total += amount
                print ('Good data added to total: '+str(amount)+' running total: '+str(total))
                

        # Close the file.
        infile.close()

        # Print the total.
        print(f'Total: {total:.2f}')
        
    except IOError:
        print('An error occured trying to read the file.')

    except ValueError:
        #print(err)
        print('Non-numeric data found in the file.')

    except:
        print('An error occured.')

# Call the main function.
if __name__ == '__main__':
    main()
