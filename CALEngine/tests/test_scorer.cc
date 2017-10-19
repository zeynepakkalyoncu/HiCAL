#include <iostream>
#include <chrono>
#include "../src/scorer.h"
#include "../src/utils/feature_parser.h"
using namespace std;

int main(int argc, char *argv[]){
    int threads = atoi(argv[2]);
    auto start = std::chrono::steady_clock::now();
    cerr<<"Loading document features on memory"<<endl;
    auto dataset = CAL::utils::BinFeatureParser(argv[1]).get_all();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds> 
        (std::chrono::steady_clock::now() - start);

    cerr<<"Read "<<dataset->size()<<" docs in "<<duration.count()<<"ms"<<endl;

    float avg = 0.0;
    for(int i = 0;i<10;i++){
        vector<int> results;
        set<int> judgments;
        for(int j = 0;j<i*500;j++){
            judgments.insert(rand() % dataset->size());
        }
        vector<float> weights(dataset->size());
        for(float &wt: weights)
            wt = (float)rand()/(float)(RAND_MAX);

        start = std::chrono::steady_clock::now();
        Scorer::rescore_documents(*dataset, weights, threads, 100, judgments, results);
        duration = std::chrono::duration_cast<std::chrono::milliseconds> 
            (std::chrono::steady_clock::now() - start);
        cerr<<"Rescored "<<dataset->size()<<" documents in "<<duration.count()<<"ms"<<endl;
        avg += duration.count();
    }
    cerr<<"Average Rescoring Time: "<<avg/10<<endl;
}
