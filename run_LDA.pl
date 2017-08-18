#!/usr/bin/perl -w
use strict;
use warnings;
use English;

my $Rscript = "/hwfssz1/ST_META/PN/zhujiahui/R/bin/Rscript";

my ($train_set,$test_set,$train_group,$test_group,$out)=@ARGV;

LDA:{
	open ERR,"$Rscript /hwfssz1/ST_META/PN/zhujiahui/meta-analysis/test-cOMG/LDA.R $train_set $test_set $train_group $test_group $out 2>&1|";

#my $count=`wc -l err.or`;
#$count =~ /^\d+/;
#$count = $MATCH;
#if($count == 4){last LDA;}
#open ERR,"err.or";
	my @err;my $count=0;
	while(<ERR>){
		chomp;
		$count++;
		if(/(\s*)variables(\s+)/){
			my $num=$POSTMATCH;
			$num =~ s/appear to be constant within groups//;
			@err=split /\s+/,$num;
		}
	}
	print join "\t",@err;
	close ERR;
	if($count!=4){last LDA;}
	open IN1,$train_set;
	open IN2,$test_set;
	open OUT1,">$train_set.out";
	open OUT2,">$test_set.out";
	my ($c,$i)=(0,0);
	my $head1=<IN1>;
	my $head2=<IN2>;
	print OUT1 $head1;
	print OUT2 $head2;
	while(<IN1>){
		my $line1=$_;
		my $line2=<IN2>;
		$c++;
		if($i <=$#err){
		if($c == $err[$i]){
			$i++;next;
		}}
		print OUT1 $line1;
		print OUT2 $line2;
	}	
	close IN1;close IN2;
	close OUT1;close OUT2;
	$train_set.=".out";
	$test_set.=".out";
#`rm err.or`;
	redo LDA;
}
