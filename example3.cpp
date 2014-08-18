#include <iostream>
#include "TFile.h"
#include "TH2D.h"

extern "C"{
void get_2d_hist_content(const char* root_file_name, const char * th2d_name, int n, double * content){
    TFile file(root_file_name);
    if (file.IsOpen()){
        if(file.Get(th2d_name)){
            TH2D* hist=(TH2D*)file.Get(th2d_name)->Clone();
            if (n==hist->fN){
                for (int i=0;i<n;i++){
                    content[i]=hist->GetAt(i);
                }
            
            }
            else{
                std::cout << "Number provided doesn't equal the number of elements in the 2d hist"<< std::endl;
            }
        }
        else{
            std::cout<< "Couldn't find hist name \"" << th2d_name <<"\"" << std::endl; 
        }
    }
    else{
        std::cout << "Couldn't open rootfile: \"" << root_file_name <<"\"" << std::endl;
    }
    file.Close();
}
}
