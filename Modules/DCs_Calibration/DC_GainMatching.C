///////////////////////GainMatching Scrip/////////////////////////
#include <stdio.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <string>
#include <TString.h>
#include <algorithm>
#include <sstream>
#include <TROOT.h>
#include <TStyle.h>
#include <TFile.h>
#include <TObject.h>
#include <TTree.h>
#include <TCanvas.h>
#include <TMath.h>
#include <TSpectrum.h>
#include <TH1.h>
#include <TH2.h>
#include <TF1.h>
#include <TGraph.h>
#include <TGraphErrors.h>
#include <TMultiGraph.h>
#include <TChain.h>
#include <TProfile.h>
#include <TFile.h>
#include <vector>

vector <double> vQMax;
vector <int> vQNMax;

Int_t DC_QVM;
Float_t DC_QV[160];
UShort_t DC_QVN[160];

TH1F *h[160];

double A[160];
double B[160];
double C[160];

void ReadCalib(int DC_number)
{
  double a, b, c;
  char file_name[256];
  sprintf(file_name,"/Users/dani/Dani/FISICA/INVESTIGACION/DOCTORADO/TESIS_NUCLEAR/e753/Analysis_Dani/Calibs/DC%d.cal",DC_number);
  ifstream factorsfile(file_name);
  string line;
  int counter =0;
  for(int i=0;i<15;i++)
    {
      getline(factorsfile,line);
      cout<<line<<endl;
    }
  while(getline(factorsfile,line))
    {
      istringstream read (line);
      read>>a>>b>>c;
      A[counter]=a;
      B[counter]=b;
      C[counter]=c;
      counter++;
    }


}

TChain *t1 = NULL;
Int_t Ta;

void AccessData(int file_number)
{
  cout << "Run: " << file_number <<endl;
  char name[200];
  t1 = NULL;
  Ta = 0;
  t1 =new TChain("AD");
  Bool_t fExist = true;
  for(Int_t j=0;j<999&&fExist;j++)
    {
      //sprintf(name,"/data/mugastX/e744/acquisition/run/RootA//r%04d_%03da.root",file_number,j);
     sprintf(name,"/Users/dani/Dani/FISICA/INVESTIGACION/DOCTORADO/TESIS_NUCLEAR/e753/Analysis_Dani/RootA/r%04d_%03da.root",file_number,j);
      cout << name << endl;
      ifstream mfile;
      mfile.open(name);
      if(mfile)
        mfile.close();
      else
        fExist=false;
      if(fExist)
        {
          cout << "Adding " << name << endl;
          t1->Add(name);
          Ta = (Int_t) (t1->GetEntries());
          cout << "Entries " << Ta/1000 << "k "  << endl;
        }
    }
}
void ReadData(int DC_number)
{
  vQMax.clear();
  vQNMax.clear();
  int qnmax;
  double qqmax;
  char QMname[256];
  char Qname[256];
  char QNname[256];
  sprintf(QMname,"DC%d_QVM",DC_number);
  sprintf(Qname,"DC%d_QV",DC_number);
  sprintf(QNname,"DC%d_QVN",DC_number);

  t1->SetBranchStatus("*",0);
  t1->SetBranchStatus(QMname,1);
  t1->SetBranchStatus(Qname,1);
  t1->SetBranchStatus(QNname,1);

  t1->SetBranchAddress(QMname,&DC_QVM);
  t1->SetBranchAddress(Qname,DC_QV);
  t1->SetBranchAddress(QNname,DC_QVN);

  for(int i=0;i<Ta;i++)
    {
      t1->GetEntry(i);
      if(i%1000==0)
        cout<<"\r"<<"Reading: "<<1.*i/Ta*100.<<" %"<<flush;

      qqmax=0;
      qnmax=-1;
      for(int m=0;m<DC_QVM;m++)
        if(qqmax<DC_QV[m])
        {
          qqmax = DC_QV[m];
          qnmax = DC_QVN[m];
        }
      if(qnmax>-1)
        {
          vQMax.push_back(qqmax);
          vQNMax.push_back(qnmax);
        }
    }

}

void Draw_MaxQ(int file_number)
{
  AccessData(file_number);
  TH2F *h2[4];
  char hname[256];
  for(int i=0;i<4;i++)
    {
      ReadData(i);
      sprintf(hname,"h_row%d",i);
      h2[i]= new TH2F(hname,hname,160,0,160,500,0,16000);
      for(int j=0;j<int(vQMax.size()+0.5);j++)
        h2[i]->Fill(int(vQNMax[j]),vQMax[j]);
    }
  TCanvas *c2 = new TCanvas();
  c2->Divide(2,2);
   for(int i=0;i<4;i++)
    {
      gStyle->SetPalette(55);
      c2->cd(i+1);
      h2[i]->Draw("col");
    }
}


void DC_Pedestal_Subtraction(int file_number)
{/*
  AccessData(file_number);
  char hname[256];
  for(int j=0;j<4;j++)
    {

      for(int i=0;i<160;i++)
        {
          h[i]=NULL;
          sprintf(hname,"h_pad%d_row%d",i,j);
          h[i]=new TH1F(hname,hname,6000,10,16000);
          A[i]=B[i]=C[i]=0;
        }
      ReadData(j);
      ReadCalib(j);
      for(int i=0;i<int(vQ.size());i++)
        h[int(vQN[i]+0.5)]->Fill(vQ[i]);

      for(int i=0;i<160;i++)
        {
          cout<< A[i]-h[i]->GetXaxis()->GetBinCenter(h[i]->GetMaximumBin())+10<<" "<<B[i]<<" "<<C[i]<<" // "<<j<<" ch "<<i<<endl;
        }

        }*/
}

void Constant_Gain_Factor(int file_number,int DC_Row,int PadInit, int PadEnd, double Gain, double Const_value=0)
{
  int j= DC_Row;
  for(int i=0;i<160;i++)
    A[i]=B[i]=C[i]=0;
  ReadCalib(j);
  for(int i=PadInit;i<PadEnd+1;i++)
    cout<< Const_value+(A[i]-Const_value)*Gain<<" "<<B[i]*Gain<<" "<<C[i]*Gain<<" // "<<j<<" ch "<<i<<endl;

  AccessData(file_number);
  TH2F *h2;
  char hname[256];
  ReadData(DC_Row);
  sprintf(hname,"h_row%d",DC_Row);
  h2= new TH2F(hname,hname,160,0,160,500,0,16000);
  for(int j=0;j<int(vQMax.size()+0.5);j++)
    if(vQNMax[j]>=PadInit&&vQNMax[j]<=PadEnd)
      h2->Fill(int(vQNMax[j]),vQMax[j]*Gain);
    else
      h2->Fill(int(vQNMax[j]),vQMax[j]);

  TCanvas *c2 = new TCanvas();
  gStyle->SetPalette(55);
  c2->cd();
  h2->Draw("col");

}
