package com.tm.lda;

import java.io.IOException;
import java.util.Map;

public class Main {
	
	public static void main(String[] args)
	{
	    // 1. Load corpus from disk
	    Corpus corpus = null;
		try {
			corpus = Corpus.load("data/all");
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	    // 2. Create a LDA sampler
	    GibbsSampler ldaGibbsSampler = new GibbsSampler(corpus.getDocument(), 
	    		corpus.getVocabularySize());
	    // 3. Train it
	    ldaGibbsSampler.gibbs(4);
	    // 4. The phi matrix is a LDA model, you can use LdaUtil to explain it.
	    double[][] phi = ldaGibbsSampler.getPhi();
	    System.out.println("Number of interactions£º"+GibbsSampler.ITERATIONS);
	    Map<String, Double>[] topicMap = Utils.translate(phi, corpus.getVocabulary(), 200);
	    Utils.explain(topicMap);
	}

}
