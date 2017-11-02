#!/usr/bin/perl -w
use strict;
use warnings;
use English;

my $Rscript = "/path/to/your/Rscript"; ##or you can add a parameter below.

my ($train_set,$test_set,$train_group,$test_group,$out)=@ARGV; ##you can change it with Getopt::Long & FindBin qw($Bin)

my $help = "perl run_LDA.pl train.set test.set train.group test.group prefix";
if(!$train_set && !$test_set && !$train_group && !$test_group && !$out){die "$help";}
## These two line above were not in my original script.
LDA:{
	open ERR,"$Rscript /path/to/your/LDA.R $train_set $test_set $train_group $test_group $out 2>&1|";
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
	#print join "\t",@err;
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
	redo LDA;
}
`rm *.out`;
#I did not put the entire file into the swap because files I used to process had millions of lines and variables. 
#Whether there is a better way to remove uncapable variables haven't come to my mind. 
#If any brilliant minds find out how to improve it, please let me know.
